import axios from 'axios';

const state = {
    user : null,
}

const getters ={
    isAuthorized: state => !!state.user,
    stateUser: state => state.user,
}

const actions = {
    async viewMe({commit}){
        let {data} = await axios.get('/user')
        await commit('setUser', data);
    },
    async logOut({commit}){
        let user = null;
        commit('logout', user);
    }
}

const mutations = {
    setUser(state, username){
        state.user = username
    },
    logout(state, user){
        state.user = user;
    }
};

export default {
    state,
    getters,
    actions,
    mutations
}