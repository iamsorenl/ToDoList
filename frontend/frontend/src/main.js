import { createApp } from "vue";
import App from "./App.vue";
import * as BVN from "bootstrap-vue-next";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-next/dist/bootstrap-vue-next.css";

const app = createApp(App).use(router).use(BVN.createBootstrap());
for (const name of ["BButton", "BForm", "BFormCheckbox", "BFormGroup", "BFormInput", "BModal", "BTable"]) {
  app.component(name, BVN[name]);
}
app.mount("#app");
