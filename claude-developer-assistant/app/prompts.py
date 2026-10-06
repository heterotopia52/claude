# Prompt V1.0
# PYTHON_EXPLANATION_PROMPT = """
# Explain the following Python concept in detail, providing
# a clear explanation,
# an example of its usage,
# and a common mistake to avoid.
# Format your response as a JSON object
# with the following fields:
#   "concept", "explanation", "example", and "common_mistake".

# <concept>
# {concept}
# </concept>
# """

# Prompt V1.0
# PYTHON_EXPLANATION_PROMPT = """
# Explain the following Python concept:

# <concept>
# {concept}
# </concept>

# The explanation should be appropriate for a Python developer
# who understands basic functions and classes.

# Include:
# - what the concept is
# - how it works
# - a practical example
# - one common mistake
# """

# Prompt V2.0
PYTHON_EXPLANATION_PROMPT = """
You are a senior Python engineer mentoring a developer.

Explain the following Python concept:

<concept>
{concept}
</concept>

The developer already understands:
- variables
- functions
- classes
- basic object-oriented programming

Structure the explanation as follows:

1. Definition
2. Mental model
3. How it works
4. Practical example
5. Common mistake
6. When to use it
7. When NOT to use it

Do not oversimplify.
Do not introduce concepts unrelated to the requested topic.
Use technically accurate Python examples.
"""
