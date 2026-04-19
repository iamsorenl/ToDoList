<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <h1 class="text-center bg-primary text-white" style="border-radius: 10px">
        To Do List 🗒️
      </h1>
      <hr />
      <br />
      <!-- Add Task Button -->
      <b-button variant="success" @click="showAddTaskModal">Add Task</b-button>
      <br /><br />

      <!-- Task List Table -->
      <b-table striped hover :items="tasks" :fields="tableFields" caption-top>
        <template #cell(actions)="data">
          <div class="btn-group" role="group">
            <b-button variant="info" @click="editTask(data.item)">
              Update
            </b-button>
            <b-button variant="danger" @click="deleteTask(data.item.id)">
              Delete
            </b-button>
          </div>
        </template>
      </b-table>

      <!-- Footer -->
      <footer
        class="bg-primary text-white text-center"
        style="border-radius: 10px"
      >
        Copyright &copy; All Rights Reserved {{ currentYear }}.
      </footer>

      <!-- Add Task Modal -->
      <b-modal v-model="addTaskModal" title="Add a new task" hide-footer>
        <b-form @submit="onSubmit" @reset="onReset">
          <b-form-group label="Task:" label-for="form-task-input">
            <b-form-input
              id="form-task-input"
              v-model="addTaskForm.task"
              required
              placeholder="Enter Task"
            ></b-form-input>
          </b-form-group>
          <b-form-group label="Deadline:" label-for="form-deadline-input">
            <b-form-input
              id="form-deadline-input"
              v-model="addTaskForm.deadline"
              required
              placeholder="Enter Deadline"
            ></b-form-input>
          </b-form-group>
          <b-form-group>
            <b-form-checkbox v-model="addTaskForm.completed" value="true">
              Completed?
            </b-form-checkbox>
          </b-form-group>
          <b-button type="submit" variant="outline-success">Submit</b-button>
          <b-button type="reset" variant="outline-primary">Reset</b-button>
        </b-form>
      </b-modal>

      <!-- Update Task Modal -->
      <b-modal v-model="editTaskModal" title="Edit Task" hide-footer>
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate">
          <b-form-group label="Task:" label-for="form-task-edit-input">
            <b-form-input
              id="form-task-edit-input"
              v-model="editTaskForm.task"
              required
              placeholder="Enter Task"
            ></b-form-input>
          </b-form-group>
          <b-form-group label="Deadline:" label-for="form-deadline-edit-input">
            <b-form-input
              id="form-deadline-edit-input"
              v-model="editTaskForm.deadline"
              required
              placeholder="Enter Deadline"
            ></b-form-input>
          </b-form-group>
          <b-form-group>
            <b-form-checkbox v-model="editTaskForm.completed" value="true">
              Completed?
            </b-form-checkbox>
          </b-form-group>
          <b-button type="submit" variant="outline-success">Update</b-button>
          <b-button type="reset" variant="outline-primary">Cancel</b-button>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
const STORAGE_KEY = "todolist.tasks";

function loadTasks() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveTasks(tasks) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

function newId() {
  if (typeof crypto !== "undefined" && crypto.randomUUID) {
    return crypto.randomUUID();
  }
  return Date.now().toString(36) + Math.random().toString(36).slice(2);
}

export default {
  data() {
    return {
      currentYear: new Date().getFullYear(),
      tasks: [],
      addTaskForm: {
        task: "",
        deadline: "",
        completed: [],
      },
      editTaskForm: {
        id: "",
        task: "",
        deadline: "",
        completed: [],
      },
      addTaskModal: false,
      editTaskModal: false,
      tableFields: [
        { key: "task", label: "Task" },
        { key: "deadline", label: "Deadline" },
        { key: "completed", label: "Completed?" },
        { key: "actions", label: "Actions" },
      ],
    };
  },
  methods: {
    getTasks() {
      this.tasks = loadTasks();
    },
    addTask(payload) {
      const tasks = loadTasks();
      tasks.push({ id: newId(), ...payload });
      saveTasks(tasks);
      this.getTasks();
      this.addTaskModal = false;
      this.initForm();
    },
    initForm() {
      this.addTaskForm.task = "";
      this.addTaskForm.deadline = "";
      this.addTaskForm.completed = [];
    },
    onSubmit(e) {
      e.preventDefault();
      const completed = this.addTaskForm.completed.includes("true");
      this.addTask({
        task: this.addTaskForm.task,
        deadline: this.addTaskForm.deadline,
        completed,
      });
    },
    showAddTaskModal() {
      this.addTaskModal = true;
    },
    onReset(e) {
      e.preventDefault();
      this.initForm();
    },
    editTask(task) {
      this.editTaskForm.id = task.id;
      this.editTaskForm.task = task.task;
      this.editTaskForm.deadline = task.deadline;
      this.editTaskForm.completed = task.completed ? ["true"] : [];
      this.editTaskModal = true;
    },
    onSubmitUpdate(e) {
      e.preventDefault();
      const completed = this.editTaskForm.completed.includes("true");
      this.updateTask(
        {
          task: this.editTaskForm.task,
          deadline: this.editTaskForm.deadline,
          completed,
        },
        this.editTaskForm.id
      );
    },
    onResetUpdate(e) {
      e.preventDefault();
      this.editTaskModal = false;
    },
    updateTask(payload, taskId) {
      const tasks = loadTasks().map((t) =>
        t.id === taskId ? { id: taskId, ...payload } : t
      );
      saveTasks(tasks);
      this.getTasks();
      this.editTaskModal = false;
    },
    deleteTask(taskId) {
      const tasks = loadTasks().filter((t) => t.id !== taskId);
      saveTasks(tasks);
      this.getTasks();
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
