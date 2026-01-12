from kernel.state import CognitiveState
from kernel.loop import CognitiveKernel

def test_valid_state_transitions():
    kernel = CognitiveKernel()
    kernel.load_task("Test task")

    assert kernel.state == CognitiveState.INTERPRET

    kernel.run()

    assert kernel.state in (
        CognitiveState.DONE,
        CognitiveState.ERROR
    )
