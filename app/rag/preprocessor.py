def preprocess_catalog(catalog):
    """
    Convert raw SHL catalog into clean searchable documents.
    """

    documents = []

    for item in catalog:

        name = item.get("name", "")
        description = item.get("description", "")
        duration = item.get("duration", "")
        remote = item.get("remote_testing", "")
        adaptive = item.get("adaptive_irt", "")
        job_levels = ", ".join(item.get("job_levels", []))
        languages = ", ".join(item.get("languages", []))
        url = item.get("link", "")

        text = f"""
Assessment Name: {name}

Description:
{description}

Job Levels:
{job_levels}

Duration:
{duration}

Remote Testing:
{remote}

Adaptive:
{adaptive}

Languages:
{languages}
"""

        documents.append(
            {
                "text": text.strip(),
                "metadata": {
                    "name": name,
                    "url": url,
                    "duration": duration,
                    "job_levels": job_levels,
                },
            }
        )

    return documents