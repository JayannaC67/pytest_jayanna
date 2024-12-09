def color_picker(color):
    all_colors={
        "#ffffff":"white",
        "#f29111":"orrange"
    }
    return all_colors.get(color)

def company(text):
    all_company_elements = {
        "padding": "20p",
        "font-size": "14px"
    }
    return all_company_elements.get(text)