topic=widgets.Text(
    description ='topic',
    layout=widgets.Layout(width='500px')
)

tone=widgets.Dropdown(
    description ='tone',
    options=['sad','biased','neutral','casual','zesty','happy'],
    layout=widgets.Layout(width='500px')
)

AUDIENCE=widgets.Text(
    description ='Audience',
    layout=widgets.Layout(width='500px')
)
HASH=widgets.Text(
    description ='hashtag',
    layout=widgets.Layout(width='500px')
)

gen = widgets.Button(
    description='Generate Tweet',
    button_style='info',
    tooltip='Click to generate',
    layout=widgets.Layout(width='500px')

  
  def generate(b):
    output.clear_output()
    prompt = f"""You are an expert Content Writer. Generate a tweet about the topic "{topic.value}" using a "{tone.value}" tone. Include hashtag "{HASH.value}". Keep it under 200 characters."""

    with output:
        try:
            response = model.generate_content(prompt)
            tweet = response.text.strip()
            display(Markdown(f"###  Generated Tweet:\n{tweet}"))
        except Exception as e:
            display(Markdown(f"** Error:** {str(e)}"))
            
# Attach the function to the button click
gen.on_click(generate)

# Display all widgets
display(topic, tone, AUDIENCE, HASH, gen, output)
