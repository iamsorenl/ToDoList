<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SharkInfo",
  data() {
    return {
      msg: "Hello, this is Shark",
    };
  },
  methods: {
    getResponse() {
      const path = "http://localhost:5000/shark";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
