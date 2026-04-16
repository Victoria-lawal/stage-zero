from datetime import datetime, timezone

def process_data(raw_data):
    gender = raw_data.get("gender")
    probability = raw_data.get("probability")
    count = raw_data.get("count")

    # Edge case
    if gender is None or count == 0:
        return None

    is_confident = probability >= 0.7 and count >= 100

    return {
        "name": raw_data.get("name"),
        "gender": gender,
        "probability": probability,
        "sample_size": count,
        "is_confident": is_confident,
        "processed_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    }