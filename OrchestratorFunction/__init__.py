import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    joke = yield context.call_activity('GetJoke', None)
    processed_joke = yield context.call_activity('ProcessJoke', joke)
    yield context.call_activity('LogJoke', processed_joke)
    yield context.call_activity('SendJoke', processed_joke)

main = df.Orchestrator.create(orchestrator_function)