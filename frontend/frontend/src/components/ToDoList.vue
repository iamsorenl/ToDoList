<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <h1 class="text-center bg-primary text-white" style="border-radius: 10px">
        To Do List 🗒️
      </h1>
      <hr />
      <br />

      <!-- Add Task Button -->
      <b-button variant="success" @click="showAddTaskModal">Add</b-button>
      <br /><br />

      <!-- Task List Table -->
      <b-table
        striped
        hover
        :items="tasks"
        :fields="tableFields"
        caption-top
      ></b-table>

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
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="primary">Reset</b-button>
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
      addTaskModal: false,
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
    addTask(payLoad) {
      const path = "http://localhost:5000/tasks";
      axios
        .post(path, payLoad)
        .then(() => {
          this.getTasks();
          this.addTaskModal = false; // Close the modal
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
    onReset() {
      this.initForm();
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
