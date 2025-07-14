def gather_info_prompt(name, email, phone, experience, position, location, tech_stack):
    return f"""
You are a technical hiring assistant. A candidate has provided the following information:
- Full Name: {name}
- Email: {email}
- Phone: {phone}
- Years of Experience: {experience}
- Desired Position: {position}
- Current Location: {location}
- Tech Stack: {tech_stack}

Based on this information, generate 3-5 technical questions tailored to assess the candidate’s proficiency in the listed technologies.
Be specific and ensure the questions are relevant to the technologies mentioned.
"""
