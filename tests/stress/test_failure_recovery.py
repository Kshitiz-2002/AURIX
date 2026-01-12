from kernel.loop import CognitiveKernel

class FailingPlanner:
    def generate_plan(self, goal, constraints=""):
        raise Exception("Planner failure")

def test_kernel_handles_planner_failure():
    kernel = CognitiveKernel()
    kernel.planner = FailingPlanner()

    kernel.load_task("Trigger failure")

    try:
        kernel.run()
    except Exception:
        assert False, "Kernel should not crash"
