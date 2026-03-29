from fastapi import APIRouter
from app.models.schemas import UserRequest, GeneratedResponse
from app.services.classifier import classify_domains_and_difficulty
from app.services.retriever import retrieve_context
from app.services.generator import generate_question
from app.services.validator import validate_output
from app.services.csv_logger import log_to_csv

router = APIRouter()

@router.post("/generate", response_model=GeneratedResponse)
def generate(req: UserRequest):

    # Step 1: Validate + normalize domains and difficulty
    domains, difficulty = classify_domains_and_difficulty(
        req.domains,
        req.difficulty
    )

    # Step 2: Prepare query for RAG retrieval
    query_text = " ".join(domains) + f" difficulty {difficulty}"

    # Step 3: Retrieve context from Pinecone
    context = retrieve_context(query_text)

    # Step 4: Generate question using Gemini + RAG
    raw_output = generate_question(domains, difficulty, context)

    # Step 5: Validate output
    result = validate_output(raw_output)

    # Fallback if invalid
    if result is None:
        result = {
            "question": "Generation failed.",
            "difficulty": difficulty,
            "domains": domains
        }

    # Step 6: Save to CSV
    log_to_csv(result["question"], result["difficulty"], result["domains"])

    # Step 7: Return response
    return result
