<template>
  <div id="header">
    <div class="logo">
      <p>KakaoTalk Analysis</p>
    </div>
    <div class="menu">
      <ul>
        <li>Home</li>
        <li>Analysis</li>
        <li>Project</li>
      </ul>
    </div>
    <div class="link">
      <a href="#"><b-icon icon="github"/></a>
    </div>
  </div>
</template>
<style lang="scss" scoped>
  * {
    margin: 0 auto;
    padding: 0;
  }
  #header {
    $height: 80px;
    height: $height;
    width: 100%;
    border-bottom: 1px solid #ddd;
    * {
      height: $height;
      float: left;
      padding: 0 10px;
    }
    .logo {
      p {
        font-size: 25px;
        height: $height;
        line-height: $height;
      }
    }
    .menu {
      ul{
        height: $height;
        li {
          list-style: none;
          padding: 0 20px;
          text-align: center;
          float: left;
          line-height: $height;
          transition: .3s;
          &:hover {
            cursor: pointer;
            background-color: #EEE;
          }
        }
      }
    }
    .link {
      float:right;
      a {
        color: #000;
        text-decoration: none;
        line-height: $height;
      }
    }
  }
</style>
<script>
export default {
  name: 'Header',
  components: {

  }
}
</script>