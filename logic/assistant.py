from config import CFG
import google.generativeai as genai


class AssistantError(RuntimeError):
    pass


def explain_queue(question: str, context_block: str) -> str:
    if not CFG.gemini_key:
        raise AssistantError(
            "GEMINI_API_KEY is not set. Add it to .env and restart Streamlit."
        )

    try:
        # Configure Gemini
        genai.configure(api_key=CFG.gemini_key)

        model = genai.GenerativeModel(
            model_name=CFG.gemini_model,
            system_instruction=(
                "You are an operations analyst. "
                "Give concise, actionable guidance in bullet points."
            ),
        )

        prompt = (
            f"Question:\n{question}\n\n"
            f"Context:\n{context_block}"
        )

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.4,
            },
        )

        if not response.text or not response.text.strip():
            raise AssistantError("AI returned an empty response.")

        return response.text

    except Exception as e:
        raise AssistantError(f"AI request failed: {e}") from e
