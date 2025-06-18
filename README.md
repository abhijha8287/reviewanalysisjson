# 🔍 Review Analysis Bot (JSON Schema Version)

This Streamlit app uses **OpenAI GPT-4 + LangChain** to break down any written review into structured insights such as key themes, sentiment, pros and cons, and a summary — all validated using a **custom JSON schema**.

🔗 **Live App**: [https://reviewanalysisbyabhishek.streamlit.app/](https://reviewanalysisbyabhishek.streamlit.app/)

> ⚠️ If the app is inactive or sleeping, click once or refresh to wake it. Streamlit apps sleep after inactivity.

---

## 🚀 What's New in This Version?

✅ **JSON Schema for Structured Output**  
- The app uses a **dictionary-based JSON schema** instead of `pydantic.BaseModel` to define the output format.
- Offers flexibility without requiring additional typing libraries.

✅ **Enum Constraint for Sentiment**  
- The sentiment field only allows `"pos"` or `"neg"` using `enum`.

✅ **Optional Fields Handled Properly**  
- Uses `type: ["string", "null"]` and `["array", "null"]` for optional fields like `name`, `pros`, and `cons`.

✅ **Minimal Dependencies**  
- No need to import and define Python classes — pure dictionary-based validation for those who prefer lighter codebases.

---

## 💡 What This App Does

Paste any review into the input box, and the bot will return:

- 🎯 **Sentiment**: `"pos"` or `"neg"` (positive or negative)
- 🔍 **Key Themes**: List of discussed topics
- ✅ **Pros** *(optional)*: Advantages/strengths
- ❌ **Cons** *(optional)*: Drawbacks
- 🧾 **Summary**: Short human-like explanation
- 🧑 **Name** *(optional)*: Reviewer's name if available



