<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer
        expand-on-hover
        rail
      >
        <v-list>
          <v-list-item
            prepend-avatar=""
            title="null"
            subtitle="null"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-folder" title="My Files" value="myfiles"></v-list-item>
          <v-list-item prepend-icon="mdi-account-multiple" title="Shared with me" value="shared"></v-list-item>
          <v-list-item prepend-icon="mdi-star" title="Starred" value="starred"></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main style="height: 100vh">
        <MainPage/>
        <v-banner v-if="hasUserInfo && !shouldRegister"
                  color="pink-darken-1"
                  icon="mdi-account-box"
                  lines="two"
        >
          <v-banner-text>
            To use "Chatter", Please register to server!
          </v-banner-text>

          <v-banner-actions>
            <v-btn @click="shouldRegister=!shouldRegister">Register</v-btn>
          </v-banner-actions>
        </v-banner>

        <Register v-else/>
      </v-main>
    </v-layout>
  </v-card>
</template>

<script setup lang="ts">/**
 * This component just checks user information-related.
 * Not actual be seen component!
 */
import {ref} from "vue";
import Register from "@/components/Register.vue";

const hasUserInfo = ref(true);
const shouldRegister = ref(false);
</script>

<style scoped>

</style>
