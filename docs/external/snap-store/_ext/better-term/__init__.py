from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
import sphinx

def parse_contents(contents):
    command_output = []
    out = []

    while contents:
        line = contents[0]
        contents = contents[1:]
        if line.startswith(':input: '):
            out.append(command_output)
            out.append([line])
            command_output = []
        else:
            command_output.append(line)

    out.append(command_output)
    return out

class TerminalOutput(SphinxDirective):

    required_arguments = 0
    optional_arguments = 0
    has_content = True
    option_spec = {
        "input": directives.unchanged,
        "user": directives.unchanged,
        "host": directives.unchanged,
        "scroll": directives.unchanged,
    }

    @staticmethod
    def input_line(prompt_text, command):

        inpline = nodes.container()
        inpline["classes"].append("input")

        # To let the prompt be styled separately in LaTeX, it needs to be wrapped in a
        # container. This adds an extra div to the HTML output, but what's a few bytes
        # between friends?
        prompt_container = nodes.container()
        prompt_container["classes"].append("prompt")
        prompt = nodes.literal(text=prompt_text)
        prompt_container.append(prompt)

        inpline.append(prompt_container)
        inp = nodes.literal(text=command)
        inp["classes"].append("command")
        inpline.append(inp)
        # inpline.append(nodes.paragraph())
        return inpline

    def run(self):
        # if :user: or :host: are provided, replace those in the prompt

        command = "" if "input" not in self.options else self.options["input"]
        user = "user" if "user" not in self.options else self.options["user"]
        host = "host" if "host" not in self.options else self.options["host"]
        prompt_text = user + "@" + host + ":~$ "
        if user == "root":
            prompt_text = prompt_text[:-2] + "# "

        out = nodes.container()
        out["classes"].append("terminal")
        # The super-large value for linenothreshold is a major hack since I can't
        # figure out how to disable line numbering and the linenothreshold kwarg seems
        # to be required.
        out.append(sphinx.addnodes.highlightlang(lang="text", force=False, linenothreshold=10000))
        if "scroll" in self.options:
            out["classes"].append("scroll")

        # Add the original prompt and input

        out.append(self.input_line(prompt_text, command))
        # breakpoint()
        only_input = all((line.startswith(":input: ") for line in self.content))
        if only_input:
            out.append(nodes.paragraph())
        # Go through the content and append all lines as output
        # except for the ones that start with ":input: " - those get
        # a prompt

        parsed_content = parse_contents(self.content)

        for blob in parsed_content:
            if not blob:
                continue
            if blob[0].startswith(':input: '):
                out.append(self.input_line(prompt_text, blob[0][8:]))
            else:
                out.append(nodes.literal_block(text='\n'.join(blob)))
            if only_input:
                out.append(nodes.paragraph())
        return [out]


def setup(app):
    app.add_directive("term", TerminalOutput)

    return {"version": "0.1", "parallel_read_safe": True,
            "parallel_write_safe": True}
