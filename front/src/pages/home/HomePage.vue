<template>
  <div class="home"> 
    <h1>{{ greeting }}</h1>
    <section>
      <select v-model="selectedUser">
        <option :value="null" disabled >Select User</option>
        <option v-for="user in this.users" :value="user" :key="user.id">
            {{user.name }}
          </option>
      </select>
    </section>
    <button @click="onButtonClicked">GET MY NOTES</button>
    
  </div>
</template>

<script>
import config from '@/config.js';
export default {
  name: 'Home',
  data() {
    return {
    greeting:"WELCOME",
    users:[],
    selectedUser: null,
    currentUser: localStorage.userName
    };
  },

  mounted(){
    this.loadData();
  },
methods: {
  async loadData() {
  
    
    const response = await fetch(`${config.API_PATH}/user`)
    this.users = await response.json()
  /**
   * 
   *  this.users = [
      {
        id: "user-1",
        name:"Pepa",
      },
      {
        id:"user-2",
        name:"Pepe",
      },
   *  ];
   * 
   */
   
   
  },

  onButtonClicked(){
    localStorage.userId = this.selectedUser.id;
    localStorage.userName = this.selectedUser.name;
    this.$root.$forceUpdate();
    this.$router.push ("/notes")
    }
  }
};
</script>

<style scoped>

h1 {
    font-family: Arial, Helvetica, sans-serif;
    border: 5px double gray;
    border-radius: 1em;
    font-size: 2em;
    margin-top: 80px;
    text-align: center;
    text-transform: capitalize; 
}
button{
  margin-top: 80px;
  font-size: 1.5em;
  border-radius: 0.5em;
}

</style>
