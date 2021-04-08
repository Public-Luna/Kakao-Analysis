<template>
  <div id="header" class="sticky-top">
    <div class="logo">
      <p><router-link to="/">KakaoTalk Analysis</router-link></p>
    </div>
    <div class="menu">
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/analysis">Analysis</router-link></li>
        <li><router-link to="/project">Project</router-link></li>
      </ul>
    </div>
    <div class="link">
      <a class="text" href="https://github.com/Public-Luna">Team: ProjectLuna</a>
      <a href="https://github.com/Public-Luna/Kakao-Analysis"><b-icon class="icon" icon="github"></b-icon></a>
    </div>
  </div>
</template>
<style lang="scss" scoped>
  * {
    margin: 0 auto;
    padding: 0;
  }
  a { text-decoration: none; color: inherit;}
  a:hover { text-decoration: none; color: inherit;}
  #header {
    $height: 80px;
    height: $height;
    width: 100%;
    background-color: #FFF;
    border-bottom: 1px solid #ddd;
    padding: 0 10px;
    &>* {
      height: $height;
      float: left;
      padding: 0 10px;
    }
    .logo {
      p {
        font-size: 25px;
        height: $height;
        line-height: $height;
        cursor: pointer;
        transition: .3s;
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
            background-color: #EEE;
          }
        }
      }
    }
    .link {
      float:right;
      display: flex;
      a {
        color: inherit;
        display: flex;
        justify-content: center;
        align-items: center;
        &.text{
          margin-right: 10px;
        }
        .icon {
          width: 30px;
          height: 30px;
        }
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