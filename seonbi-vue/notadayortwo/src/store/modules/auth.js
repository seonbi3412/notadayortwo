import jwtDecode from 'jwt-decode'
// state : data와 유사
const state = {
  token: null
}

// mutations : state를 변화시키위한 메서드(함수)
const mutations = {
  // 첫번째 인자는 state
  // 이후 인자는 payload(즉, 임의의 매개변수) 
  setToken(state, token) {
      state.token = token
  }
}

const actions = {
  // 첫번째 인자는 context (다양한)
  // 이후 인자는 payload(임의의 매개변수 값)
  login(context, token) {
    console.log('login 한다.')
      // mutation 호출 -> commit
    context.commit('setToken', token)
  },
  logout(context) {
    context.commit('setToken', null)
  }
}

const getters = {
  options(state) {
    return {
      headers: {
        Authorization: `JWT ${state.token}`
      }
    }
  },
  user(state) {
    if (state.token) {
      return jwtDecode(state.token)
    }
    return false
  }
}

export default {
  state,
  mutations,
  actions,
  getters
}