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
        Copyright &copy; All Rights Reserved 2023.
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
import axios from "axios";

export default {
  data() {
    return {
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
    // GET function
    getTasks() {
      const path = "http://localhost:5000/tasks";
      axios
        .get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    // POST function
    addTask(payload) {
      const path = "http://localhost:5000/tasks";
      axios
        .post(path, payload)
        .then(() => {
          this.getTasks();
          this.addTaskModal = false;
          this.initForm();
        })
        .catch((err) => {
          console.error(err);
        });
    },
    initForm() {
      this.addTaskForm.task = "";
      this.addTaskForm.deadline = "";
      this.addTaskForm.completed = [];
    },
    onSubmit(e) {
      e.preventDefault();
      let completed = false;
      if (this.addTaskForm.completed.includes("true")) {
        completed = true;
      }
      const payload = {
        task: this.addTaskForm.task,
        deadline: this.addTaskForm.deadline,
        completed: completed,
      };
      this.addTask(payload);
    },
    showAddTaskModal() {
      this.addTaskModal = true;
    },
    onReset(e) {
      e.preventDefault();
      this.initForm();
    },
    // Edit Task Modal
    editTask(task) {
      this.editTaskForm.id = task.id;
      this.editTaskForm.task = task.task;
      this.editTaskForm.deadline = task.deadline;
      this.editTaskForm.completed = task.completed ? ["true"] : [];
      this.editTaskModal = true;
    },
    onSubmitUpdate(e) {
      e.preventDefault();
      let completed = false;
      if (this.editTaskForm.completed.includes("true")) {
        completed = true;
      }
      const payload = {
        task: this.editTaskForm.task,
        deadline: this.editTaskForm.deadline,
        completed: completed,
      };
      this.updateTask(payload, this.editTaskForm.id);
    },
    onResetUpdate(e) {
      e.preventDefault();
      this.editTaskModal = false;
    },
    updateTask(payload, taskId) {
      const path = `http://localhost:5000/tasks/${taskId}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getTasks();
          this.editTaskModal = false;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    // Delete Task
    deleteTask(taskId) {
      const path = `http://localhost:5000/tasks/${taskId}`;
      axios
        .delete(path, { withCredentials: true })
        .then(() => {
          this.getTasks();
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
