import google.generativeai as genai

genai.configure(api_key='gemini_api-key')

class Generator:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.prompt = """Consider You are a Tutor , The user will ask some questions and I will provide a related content to that question."""
    
    def smart_mode(self,query,contents):
        self.mode = f"""You have to generate up to 50 words content smartly that should answer the users need.Just give answer to question. No extra words\nQuestion asked is {query}"""
        self.info = "".join(content[0] for content in contents)
        self.response = self.model.generate_content(self.prompt+self.mode+self.info)

        self.chat = str(self.response.text)
        return self.chat
    
    def turbo_mode(self,query,contents):
        self.mode = f"""You have to generate up to 250 words content that should answer the users need.Just give detailed answer to question. No extra words\nQuestion asked is {query}"""
        self.info = "".join(content[0] for content in contents)
        self.response = self.model.generate_content(self.prompt+self.mode+self.info)

        self.chat = str(self.response.text)
        return self.chat
