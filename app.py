import openai
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ReactフロントエンドのURLを許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/municipality/{name}")
async def get_municipality_info(name: str):
    try:
        # 自治体紹介文を取得
        description_res = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは日本の観光案内人です。"},
                {"role": "user", "content": f"{name}を50文字以上、100文字以内で紹介してください。文字数が全角で50文字以上、100文字以内になっているか、カウントをしてください。満たしていなければ、再生成してください。"}
            ]
        )
        description = description_res.choices[0].message.content

        # 名所・名産品を取得
        highlight_res = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは日本の観光案内人です。"},
                {"role": "user", "content": f"{name}の名所または名産品を3つ、箇条書きで教えてください。"}
            ]
        )
        highlight_text = highlight_res.choices[0].message.content
        highlights = [{"name": item.strip("- ").strip()} for item in highlight_text.split("\n") if item.strip()]

        return {
            "description": description,
            "highlights": highlights
        }

    except Exception as e:
        return {
            "description": f"{name}の紹介文（仮）",
            "highlights": [
                {"name": "名所1"},
                {"name": "名所2"},
                {"name": "名所3"}
            ],
            "error": str(e)
        }
