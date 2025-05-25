import openai

def suggest_improvements(yaml_str):
    prompt = f"""
You are a DevOps expert reviewing a Jenkins Job Builder YAML definition.
Suggest improvements for structure, reuse, or modern practices:

```yaml
{yaml_str}
```
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response["choices"][0]["message"]["content"]