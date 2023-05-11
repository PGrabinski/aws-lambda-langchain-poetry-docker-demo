from aws_cdk import core
from cdk import MyStack

app = core.App()
MyStack(app, "MyStack")
app.synth()