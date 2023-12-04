import {createStore} from "vuex";

export interface State {
  token: string | null;
}

export const store = createStore<State>({
  state: {
    token: localStorage.getItem("auth/token"),
  },
  mutations: {
    setToken(state, token: string) {
      state.token = token;
    },
    removeToken(state) {
      state.token = null;
    },
  },
});
