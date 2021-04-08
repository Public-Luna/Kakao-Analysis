<template>
  <div id="footer">
    <p>powered by LunaB</p>
    <p>Team: ProjectLuna</p>
    <p>SAI</p>
    <p>2021.04.06</p>
    <p>luna20617@gmail.com</p>
  </div>
</template>
<style lang="scss" scoped>
  * {
    margin: 0 auto;
    padding: 0;
  }
  #footer {
    $height: 60px;
    height: $height;
    width: 100%;
    background-color: #FFF;
    border-top: 1px solid #ddd;
    padding: 0 10px;
    p {
      float: left;
      height: $height;
      line-height: $height;
      margin: 0 10px;
    }
  }
</style>
<script>
export default {
  name: 'Footer',
  components: {

  }
}
</script>