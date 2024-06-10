
import mlrun
def pipeline():
    project = mlrun.get_current_project()
    func = project.get_function("test-func",ignore_cache=True)
    mlrun.run_function(func)
