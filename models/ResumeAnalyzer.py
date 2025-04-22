d = {
    "score": 9,
    "strengths": ["Relevant work experience with impactful projects", "Strong technical skills and diverse technology stack", "Strong educational background with high GPA"],
    "suggestions": ["Consider adding quantifiable achievements to work experience bullet points", "Include a summary section highlighting key strengths and career objectives"],
    "Constructive Criticism": ["Provide more context on the scale and impact of your projects, such as user adoption rates or business outcomes"]
}

class Resume:
    def __init__(self, score, strengths, suggestions, constructive_criticism):
        self.score = score
        self.strengths = strengths
        self.suggestions = suggestions
        self.constructive_criticism = constructive_criticism

    @classmethod
    def setter(cls, data:dict):
        return cls(
            score=data.get("score",0),
            strengths=data.get("strengths", []),
            suggestions=data.get("suggestions", []),
            constructive_criticism=data.get("Constructive Criticism", [])
        )
