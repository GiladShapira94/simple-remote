
import mlrun
def pipeline():
    project = mlrun.get_or_create_project()
    func = project.get_function("test-func",ignore_cache=True)
    mlrun.run_function(func)
