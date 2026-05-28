"""
Day 1 — LLM API Foundation
AICB-P1: AI Practical Competency Program, Phase 1

Instructions:
    1. Fill in every section marked with TODO.
    2. Do NOT change function signatures.
    3. Copy this file to solution/solution.py when done.
    4. Run: pytest tests/ -v
"""

import os
import sys
import time
from typing import Any, Callable
from openai import OpenAI

# ---------------------------------------------------------------------------
# Estimated costs per 1K OUTPUT tokens (USD) — update if pricing changes
# ---------------------------------------------------------------------------
COST_PER_1K_OUTPUT_TOKENS = {
    "gpt-4o": 0.010,
    "gpt-4o-mini": 0.0006,
}

OPENAI_MODEL = "gpt-4o"
OPENAI_MINI_MODEL = "gpt-4o-mini"


# ---------------------------------------------------------------------------
# Cấu hình Client bảo mật (Tự động nhận diện môi trường Test hoặc Chạy thật)
# ---------------------------------------------------------------------------
IS_TESTING = "pytest" in sys.modules or "unittest" in sys.modules

if IS_TESTING:
    # Khi chạy kiểm thử tự động: Dùng key mock để tránh kẹt tiến trình test
    client = OpenAI(api_key="mock-key-for-testing")
else:
    # Khi chạy thủ công ngoài terminal: Yêu cầu nhập key bảo mật từ bàn phím
    print("=" * 60)
    print(" CẤU HÌNH XÁC THỰC OPENROUTER API ")
    print("=" * 60)
    
    env_key = os.getenv("OPENAI_API_KEY")
    if env_key:
        print("-> Đã tìm thấy API Key lưu trong biến môi trường.")
        user_key = env_key
    else:
        user_key = input("Vui lòng dán mã API Key của bạn (sk-or-v1-...) vào đây: ").strip()
        
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=user_key
    )
    print("-> Kết nối OpenRouter thành công!\n")


# ---------------------------------------------------------------------------
# Task 1 — Call GPT-4o
# ---------------------------------------------------------------------------
def call_openai(
    prompt: str,
    model: str = OPENAI_MODEL,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    """
    Call the OpenAI Chat Completions API and return the response text + latency.
    """
    start_time = time.time()
    
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        stream=False
    )
    
    latency = time.time() - start_time
    response_text = response.choices[0].message.content or ""
    
    return response_text, latency


# ---------------------------------------------------------------------------
# Task 2 — Call GPT-4o-mini
# ---------------------------------------------------------------------------
def call_openai_mini(
    prompt: str,
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 256,
) -> tuple[str, float]:
    """
    Call the OpenAI Chat Completions API using gpt-4o-mini and return the
    response text + latency.
    """
    return call_openai(
        prompt=prompt,
        model=OPENAI_MINI_MODEL,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens
    )


# ---------------------------------------------------------------------------
# Task 3 — Compare GPT-4o vs GPT-4o-mini
# ---------------------------------------------------------------------------
def compare_models(prompt: str) -> dict:
    """
    Call both gpt-4o and gpt-4o-mini with the same prompt and return a
    comparison dictionary.
    """
    gpt4o_response, gpt4o_latency = call_openai(prompt)
    mini_response, mini_latency = call_openai_mini(prompt)
    
    # Cost estimate formula based on requirements:
    # (len(response.split()) / 0.75) / 1000 * COST_PER_1K_OUTPUT_TOKENS["gpt-4o"]
    words_count = len(gpt4o_response.split())
    estimated_tokens = words_count / 0.75
    gpt4o_cost_estimate = (estimated_tokens / 1000) * COST_PER_1K_OUTPUT_TOKENS["gpt-4o"]
    
    return {
        "gpt4o_response": gpt4o_response,
        "mini_response": mini_response,
        "gpt4o_latency": gpt4o_latency,
        "mini_latency": mini_latency,
        "gpt4o_cost_estimate": gpt4o_cost_estimate
    }


# ---------------------------------------------------------------------------
# Task 4 — Streaming chatbot with conversation history
# ---------------------------------------------------------------------------
def streaming_chatbot() -> None:
    """
    Run an interactive streaming chatbot in the terminal.
    Maintains the last 3 conversation turns in history.
    """
    history = []
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting chatbot. Goodbye!")
            break
            
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
            
        if not user_input:
            continue
            
        # Build message payload for API from history
        messages = []
        for turn in history:
            messages.append({"role": "user", "content": turn["user"]})
            messages.append({"role": "assistant", "content": turn["assistant"]})
            
        # Append current user prompt
        messages.append({"role": "user", "content": user_input})
        
        # Call streaming API
        stream = client.chat.completions.create(
            model=OPENAI_MINI_MODEL,
            messages=messages,
            stream=True
        )
        
        print("Bot: ", end="", flush=True)
        assistant_reply = ""
        
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            print(delta, end="", flush=True)
            assistant_reply += delta
        print()
        
        # Save this successful turn
        history.append({"user": user_input, "assistant": assistant_reply})
        
        # Maintain exactly the last 3 conversation turns
        if len(history) > 3:
            history = history[-3:]


# ---------------------------------------------------------------------------
# Bonus Task A — Retry with exponential backoff
# ---------------------------------------------------------------------------
def retry_with_backoff(
    fn: Callable,
    max_retries: int = 3,
    base_delay: float = 0.1,
) -> Any:
    """
    Call fn(). If it raises an exception, retry up to max_retries times
    with exponential backoff (base_delay * 2^attempt).
    """
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except Exception as e:
            if attempt == max_retries:
                raise e
            
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)


# ---------------------------------------------------------------------------
# Bonus Task B — Batch compare
# ---------------------------------------------------------------------------
def batch_compare(prompts: list[str]) -> list[dict]:
    """
    Run compare_models on each prompt in the list.
    """
    batch_results = []
    for prompt in prompts:
        res_dict = compare_models(prompt)
        res_dict["prompt"] = prompt
        batch_results.append(res_dict)
    return batch_results


# ---------------------------------------------------------------------------
# Bonus Task C — Format comparison table
# ---------------------------------------------------------------------------
def format_comparison_table(results: list[dict]) -> str:
    """
    Format a list of compare_models results as a readable text table.
    Truncate long text to 40 characters for readability.
    """
    def truncate(text: str, max_len: int = 40) -> str:
        text_clean = text.replace("\n", " ")
        if len(text_clean) > max_len:
            return text_clean[:max_len - 3] + "..."
        return text_clean

    # Define headers
    headers = ["Prompt", "GPT-4o Response", "Mini Response", "GPT-4o Latency", "Mini Latency"]
    
    # Create the table rows
    rows = []
    # Add Header
    rows.append(" | ".join(headers))
    # Add Separator line
    rows.append("-+-".join(["-" * len(h) for h in headers]))
    
    for item in results:
        p = truncate(item.get("prompt", ""))
        g4o = truncate(item.get("gpt4o_response", ""))
        mini = truncate(item.get("mini_response", ""))
        g4o_lat = f"{item.get('gpt4o_latency', 0.0):.3f}s"
        mini_lat = f"{item.get('mini_latency', 0.0):.3f}s"
        
        rows.append(f"{p} | {g4o} | {mini} | {g4o_lat} | {mini_lat}")
        
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# Entry point for manual testing
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    test_prompt = "Explain the difference between temperature and top_p in one sentence."
    print("=== Comparing models ===")
    result = compare_models(test_prompt)
    for key, value in result.items():
        print(f"{key}: {value}")

    # --- CHẠY BÀI TẬP 2.1 — THỬ NGHIỆM TEMPERATURE ---
    print("\n=== ĐANG CHẠY BÀI TẬP 2.1 — THỬ NGHIỆM TEMPERATURE ===")
    prompt_bai_tap = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."
    mức_temp = [0.0, 0.5, 1.0, 1.5]
    
    for t in mức_temp:
        print(f"\n--- Kết quả với Temperature = {t} ---")
        response_text, latency = call_openai(prompt=prompt_bai_tap, temperature=t)
        print(response_text)
        print(f"(Độ trễ: {latency:.2f} giây)")

    # --- KHỞI CHẠY INTERACTIVE CHATBOT ---
    print("\n=== Starting chatbot (type 'quit' to exit) ===")
    streaming_chatbot()