<template>
  <input v-model="user_name" placeholder="Please input user name!">
  <div v-bind="user_name"></div>
  <v-btn variant="outlined" @click="rrr">Register</v-btn>
</template>

<script setup lang="ts">

import {register} from "@/utils/helper";

const user_name = "";

function rrr() {
  register(user_name)
}
</script>

<style scoped>

</style>
