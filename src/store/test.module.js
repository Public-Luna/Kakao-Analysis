import ApiService from "@/common/api.service";
import UserService from "@/common/user.service";
import { FETCH_CHART } from "./actions.type";
import {
  FETCH_START,
  FETCH_END,
} from "./mutations.type";

const state = {
  chart: {
    title: '',
    labels: [],
    data: []
  },
  isLoading: true,
};

const getters = {
  chart(state) {
    return state.chart;
  },
  isLoading(state) {
    return state.isLoading;
  },
};

const actions = {
  [FETCH_CHART]({ commit }, params) {
    commit(FETCH_START);
    console.log(params)
    console.log(UserService.getToken())
    return ApiService.query('test', {
      params: {
        file_key: UserService.getToken()
      }
    })
      .then(({ data }) => {
        console.log(data)
        commit(FETCH_END, data);
      })
      .catch(error => {
        throw new Error(error);
      });
  },
};

/* eslint no-param-reassign: ["error", { "props": false }] */
const mutations = {
  [FETCH_START](state) {
    state.isLoading = true;
  },
  [FETCH_END](state, { chart }) {
    state.chart = chart;
    state.isLoading = false;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
