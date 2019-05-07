#include <tasklib/executor.h>

int main()
{
  // Create executor, the argument is the name of the executor
  tasklib::Executor executor("example1");

  // Register task "hello"
  executor.add_task("hello", [](tasklib::Context &ctx, auto &inputs, auto &outputs) {

      // Check that we been called exactly with 1 argument.
      // If not, the error message is set to context
      if (!ctx.check_n_args(1)) {
          return;
      }

      // This is body of our task, in our case, it reads the input data object
      // inserts "Hello" before the input and appends "!"
      auto& input1 = inputs[0];
      std::string str = "Hello " + input1->read_as_string() + "!";

      // Create new data instance and set it as one (and only) result
      // of the task
      outputs.push_back(std::make_unique<tasklib::MemDataInstance>(str));
  });

  // Connect to governor and serve registered tasks
  // This function is never finished.
  executor.start();
}