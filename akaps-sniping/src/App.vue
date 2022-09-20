<template>
  <div id="app">
    <AkapsHeader></AkapsHeader>
    <AkapsBody></AkapsBody>
    <AkapsFooter></AkapsFooter>
  </div>
</template>

<script>
import AkapsBody from './components/akaps-body.vue';
import AkapsFooter from './components/akaps-footer.vue';
import AkapsHeader from './components/akaps-header.vue';
export default {
  name: 'App',
  components: {
    AkapsBody,
    AkapsHeader,
    AkapsFooter
}
}
</script>

<style>
#app {
  font-family: "Atomy",Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #F6F6F6;
}

@font-face {
  font-family: "Atomy";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_four@1.0/Atomy-Bold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

@media screen and (min-device-width:320px) and (max-device-width:480px){
  html{
    font-size:12px;
  }
}
</style>
