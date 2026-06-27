from celery import shared_task

from .models import ScrapingJob
from .services import run_scraping_job


@shared_task(bind=True)
def run_scraping_job_task(self, job_id):
    try:
        job = ScrapingJob.objects.get(id=job_id)

        log = run_scraping_job(job)

        return {
            "job_id": job.id,
            "log_id": log.id,
            "status": log.status,
            "status_code": log.status_code,
            "response_time_ms": log.response_time_ms,
        }

    except ScrapingJob.DoesNotExist:
        return {
            "job_id": job_id,
            "error": "Scraping job does not exist.",
        }