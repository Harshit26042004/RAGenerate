from google import genai

client = genai.Client(api_key="AIzaSyDQ6ZmRxJd-qDQWURVarr4jTOHghtiRCf4")

class Generator:
    def __init__(self):
        self.prompt = """Consider You are a Tutor , The user will ask some questions and I will provide a related content to that question."""
    
    def smart_mode(self,query,contents):
        self.mode = f"""You have to generate up to 50 words content smartly that should answer the users need.Just give answer to question. No extra words\nQuestion asked is {query}"""
        self.info = "".join(content[0] for content in contents)
        self.response = client.models.generate_content(model="gemini-2.0-flash", contents=self.prompt+self.mode+self.info)

        self.chat = str(self.response.text)
        return self.chat
    
    def turbo_mode(self,query,contents):
        self.mode = f"""You have to generate up to 250 words content that should answer the users need.Just give detailed answer to question. No extra words\nQuestion asked is {query}"""
        self.info = "".join(content[0] for content in contents)
        self.response = client.models.generate_content(model="gemini-2.0-flash", contents=self.prompt+self.mode+self.info)

        self.chat = str(self.response.text)
        return self.chat
