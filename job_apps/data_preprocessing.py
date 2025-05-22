import pandas as pd


def extract_text(obj: list[dict]):
    return obj[0]['text']['content'] if obj else None


def map_dict(entry: dict) -> dict:
    """Map a Notion API entry to a flattened dictionary format."""
    props = entry['properties']

    company = extract_text(props['Company']['rich_text'])
    job_title = extract_text(props['Job Title']['title'])

    date = props['Date Applied']['date']
    date_applied = date['start'] if date else None

    select = props['Origin']['select']
    origin = select['name'] if select else None

    select = props['Stage']['select']
    stage = select['name'] if select else None

    job_description = extract_text(props['Job Description']['rich_text'])

    select = props['Cover letter']['select']
    cover_letter = select['name'] if select else None

    result_dict = {
        'job_title': job_title,
        'company': company,
        'date_applied': date_applied,
        'origin': origin,
        'stage': stage,
        'job_description': job_description,
        'cover_letter': cover_letter
    }
    return result_dict


def build_dataframe(results: list[dict]) -> pd.DataFrame:
    """Build a dataframe from Notion API raw entries."""
    entries_list = list(map(map_dict, results))
    return pd.DataFrame(entries_list)


if __name__ == '__main__':
    from job_apps.constants import API_HEADERS, URL_DATABASE
    from job_apps.api_requests import fetch_database_jsons
    results = fetch_database_jsons(url=URL_DATABASE, headers=API_HEADERS)

    entries = []

    for result in results:
        entry = map_dict(result)
        entries.append(entry)
