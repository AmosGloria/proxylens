import time
import httpx

from django.utils import timezone

from logs.models import RequestLog


DEFAULT_TIMEOUT = 30


def run_scraping_job(job):
    """
    Runs a simple monitoring request for a scraping job.

    This function does not parse page content yet.
    It only checks whether the target URL responds successfully,
    how long it takes, and what status code is returned.
    """

    target_url = job.target_url
    url = target_url.url

    started_at = time.perf_counter()

    try:
        headers = {
            "User-Agent": "ProxyLensBot/1.0 (+responsible monitoring)"
        }

        response = httpx.get(
            url,
            headers=headers,
            timeout=DEFAULT_TIMEOUT,
            follow_redirects=True,
        )

        elapsed_ms = int((time.perf_counter() - started_at) * 1000)
        response_size = len(response.content) if response.content else 0

        is_success = 200 <= response.status_code < 400

        log = RequestLog.objects.create(
            job=job,
            target_url=target_url,
            url=url,
            status=RequestLog.Status.SUCCESS if is_success else RequestLog.Status.FAILED,
            status_code=response.status_code,
            response_time_ms=elapsed_ms,
            response_size_bytes=response_size,
            error_message="" if is_success else f"Request returned HTTP {response.status_code}",
            retry_count=0,
        )

        job.total_runs += 1
        if is_success:
            job.successful_runs += 1
        else:
            job.failed_runs += 1

        job.last_run_at = timezone.now()
        job.save(update_fields=[
            "total_runs",
            "successful_runs",
            "failed_runs",
            "last_run_at",
            "updated_at",
        ])

        target_url.last_checked_at = timezone.now()
        target_url.save(update_fields=["last_checked_at"])

        return log

    except httpx.RequestError as exc:
        elapsed_ms = int((time.perf_counter() - started_at) * 1000)

        log = RequestLog.objects.create(
            job=job,
            target_url=target_url,
            url=url,
            status=RequestLog.Status.FAILED,
            status_code=None,
            response_time_ms=elapsed_ms,
            response_size_bytes=None,
            error_message=str(exc),
            retry_count=0,
        )

        job.total_runs += 1
        job.failed_runs += 1
        job.last_run_at = timezone.now()
        job.save(update_fields=[
            "total_runs",
            "failed_runs",
            "last_run_at",
            "updated_at",
        ])

        target_url.last_checked_at = timezone.now()
        target_url.save(update_fields=["last_checked_at"])

        return log