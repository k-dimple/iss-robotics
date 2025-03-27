from jinja2 import Environment, BaseLoader

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # Make sure we're outputting HTML or LaTeX
    if app.builder.format != 'html' and app.builder.format != 'latex':
        return
    src = source[0]
    template_renderer = Environment(loader=BaseLoader()).from_string(src)
    rendered = template_renderer.render(app.config.html_context)
    source[0] = rendered

def setup(app):
    app.connect("source-read", rstjinja)
    
    return {"version": "0.1", "parallel_read_safe": True,
            "parallel_write_safe": True}
