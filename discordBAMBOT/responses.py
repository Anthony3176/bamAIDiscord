import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello! I am the BAM-Academy discord bot!'
    
    if p_message == 'who is the best coding teacher?':
        return 'Philip Hale, of course!'

    
    if p_message == 'what can you do?':
        return 'For now, I can answer prompts you have in #AI , but soon I will be able to generate images!'
    
    if p_message == 'how do I use bam ai':
        return 'To use BAM-AI, head over to #ai. From there, use !chat and type out your prompt. Soon, BAM-AI will respond!'
    
    if p_message == 'ping':
        return 'pong'