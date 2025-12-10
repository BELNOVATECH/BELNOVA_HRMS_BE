from fastapi import HTTPException

candidates = []
candidate_id_counter = 1


async def create_candidate_service(candidate):
    global candidate_id_counter

    for c in candidates:
        if c["mobile_number"] == candidate.mobile_number:
            raise HTTPException(status_code=400, detail="Mobile number already exists")

    new_candidate = {
        "id": candidate_id_counter,
        "name": candidate.name,
        "role": candidate.role,
        "dob": candidate.dob,
        "email": candidate.email,
        "address": candidate.address,
        "mobile_number": candidate.mobile_number
    }

    candidates.append(new_candidate)
    candidate_id_counter += 1
    return new_candidate


async def get_candidates_service():
    return candidates
