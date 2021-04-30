import Vue from "vue";
import Vuex from "vuex";

import test from "./test.module";
import upload from "./upload.module"

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    test,
    upload
  }
});
