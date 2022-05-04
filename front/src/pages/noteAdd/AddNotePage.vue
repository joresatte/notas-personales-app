<template>
  <main id="notes-page">
  <section>
        <h1>{{ pagetitle }}</h1>
    <select v-model="selectedCategory">
      <option :value="null" > Select Category</option>
        <option v-for="index in categories" :key="index.id_cat" :value="index">
          {{index.name}}
          </option>
    </select>
    {{selectedCategory}}
    </section>
    <section id="notes-flex-container">
       <article id="note-item">
        <form v-on:submit.prevent="addNewNote" action="" >
          <section>
            <input  v-model="note_title" type="text" name="title-form"  placeholder="type the title here">
            <textarea v-model ="note_description" name="text-form" rows="8" cols="50"  placeholder="type the description"></textarea>
             <router-link :to="{name:'Notes'}"><button class="button-save">VOLVER</button></router-link>
            <button @click.prevent="addNewNote"  class="button-save">SAVE</button>
          </section>
        </form>
        </article>
    </section>
  </main>
</template>

<script>
import config from '@/config.js';
import Swal from 'sweetalert2';
window.Swal= Swal;
import {v4 as uuidv4} from 'uuid';

export default {
  name: 'AddNote',
  data() {
    return {
        pagetitle:"New note",
        note_title: "",
        note_description: "",
        notes_front:[],
        categories: [],
        selectedCategory: null,
    }
  },   
  mounted() {
        this.loadData()
  },

  
  methods:{
    async loadData() {
      const response = await fetch(`${config.API_PATH}/notes`)
      this.notes_front= await response.json()

      this.categories = [
        {
        id_cat: "cat-0",
        name: "No category" },
        {
        id_cat: "cat-1",
        name: "Sports" },
        {
        id_cat: "cat-2",
        name: "Music"
        },
         {
        id_cat: "cat-3",
        name: "Shops"
        }]
    },
    addNewNote(){
        if (this.note_title != "" && this.note_description != ""){
            let nextId= uuidv4()
            
            let newNote = {"id": nextId, "title": this.note_title,
                           "text": this.note_description, 
                           "user_id": localStorage.userId,
                          "id_cat": this.selectedCategory.id_cat }

            console.log("new note", newNote)

            const settings={
                method:'POST',
                body:JSON.stringify(newNote),
                headers:{
                    'Content-Type': 'application/json',
                    Authorization: localStorage.userId
                }
            }
            fetch(`${config.API_PATH}/notes`, settings)

            console.log("post a la BD hacia el endpoint - 5000/api/notes POST - ")
            console.log("obj mandado al back " + JSON.stringify(newNote))
            Swal.fire({
                      position: 'center',
                      icon: 'success',
                      title: 'Your note has been saved',
                      showConfirmButton: false,
                      timer: 1500
                      })
            //Esto redirige a la página principal de todas las notas, justo despues de añadir una nueva
            // Si no queremos la redirección, sólo hay que borrar la línea de abajo
            this.$router.push ("/notes") 
        }
              
        else{
            alert("Error! Fill in all the fields, please")
        }

        this.note_title = ""
        this.note_description= ""
        

        }
    }
}
</script>

<style scope>

  #notes-page {
    text-align: center;
    height: 100vh;
    margin-top: 10px;
    padding: 0;
    font-family: Arial, Helvetica, sans-serif;
  }
    
  #notes-flex-container {
    margin: auto;
  }

  #note-item {
    width: 85vw;
    height: 30vh;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 15px 15px;
  }

  #navegation-bar {
    display: block;
  }

  label {
    display: block;
    text-align: left;
    font-size: 20px;
    padding: 10px;
  }

  input, textarea {
    width: 85vw;
    border: 5px double gray;
    border-radius: 0.5em;
    margin-bottom: 20px;
    font-family: Arial, Helvetica, sans-serif;
  }
 
  h1 {
    font-size: 30px;
    text-align: center;
    text-transform: capitalize;
  }

  h3 {
    text-transform: uppercase;
    text-decoration: underline;
  }

  p {
    font-size: 1.2em;
    color: rgb(59, 58, 58);
    text-align: left;
  }

  .button-save {
    color: black;
    background: rgb(197, 193, 193);
    border-radius: 0.5em;
    width: 100px;
    margin-top: 30px;
    margin-right: 10px;
    padding: 5px 10px;
    font-size: 20px;
  }

</style>
