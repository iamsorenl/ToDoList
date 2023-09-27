<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- Bootswatch CDN -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lumen/bootstrap.min.css"
        integrity="sha384-GzaBcW6yPIfhF+6VpKMjxbTx6tvR/yRd/yJub90CqoIn2Tz4rRXlSpTFYMKHCifX"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            To Do List 🗒️
          </h1>
          <hr />
          <br />

          <!-- Alert Message -->
          <button type="button" class="btn btn-success btn-sm">Add</button>
          <br /><br />
          <table class="table table-hover">
            <!-- Table Head -->
            <thead>
              <tr>
                <!-- Table header cells -->
                <th scope="col">Task</th>
                <th scope="col">Deadline</th>
                <th scope="col">Completed?</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(task, index) in tasks" :key="index">
                <td>{{ task.task }}</td>
                <td>{{ task.deadline }}</td>
                <td>
                  <span v-if="task.completed">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info btn-sm">
                      Update
                    </button>
                    <button type="button" class="btn btn-danger btn-sm">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 10px"
          >
            Copyright &copy;. All Rights Reserved 2023.
          </footer>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      tasks: [],
    };
  },

  methods: {
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
  },
  created() {
    this.getTasks();
  },
};
</script>
