def smileCount(text):
    pattern = r';<)'
    matches = text.replace(pattern, '')
    return (len(text) - len(matches)) // len(pattern)

