<template>
	<!-- 首页导航 -->
	<header>
		<div class="container">
			<div class="banner">
				<a href="/">
					<img :src="BannerImg">
				</a>
			</div>
			<div class="nav-list">
				<a href="/">
					<span>主站</span>
				</a>
			</div>
			<div class="userbtn-list">
				<a href="/">
					<span>登录</span>
				</a>
				<a href="/">
					<span>注册</span>
				</a>
			</div>
		</div>
	</header>
	<div class="search-box">
		<div class="serach-btns">
			<input type="text" />
			<button>搜索</button>
		</div>
	</div>
	<div class="filter-list">
		<div class="filter-items">
			<div class="filter-class">学科：</div>
			<div class="filter-items-box">
				<span class="filter-item">全部</span>
				<span class="filter-item">语文</span>
				<span class="filter-item">数学</span>
				<span class="filter-item">英语</span>
				<span class="filter-item">物理</span>
				<span class="filter-item">化学</span>
				<span class="filter-item">生物</span>
				<span class="filter-item">历史</span>
				<span class="filter-item">地理</span>
				<span class="filter-item">政治</span>
			</div>
		</div>
		<div class="filter-items">
			<div class="filter-class">类型：</div>
			<div class="filter-items-box">
				<span class="filter-item">全部</span>
				<span class="filter-item">试卷</span>
				<span class="filter-item">导学案</span>
			</div>
		</div>
	</div>

	<hr />
	<div class="file-list">
		<div class="file-items">
			<div class="filte-item-box">
				1
			</div>
			<div class="filte-item-box">
				2
			</div>
			<div class="filte-item-box">
				3
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import BannerImg from "./assets/banner.jpg"

</script>

<style scoped lang="less">
.container {
	width: 1100px;
	margin: 0 auto;
	display: flex;
	justify-content: space-between;
	align-items: center;
	height: 52px;
	.banner {
		img {
			width: 25px;
			height: 25px;
		}
	}
	.nav-list {
		padding-left: 50px;
		flex: 1;
		display: flex;
		justify-content: start;
		align-items: center;
	}
	.userbtn-list {
		a {
			margin: 0 5px;
		}
	}
}
.search-box {
	height: 100px;
	display: flex;
	justify-content: center;
	align-items: center;
}
.filter-list {
	.filter-items {
		width: 1100px;
		margin: 0 auto;
		padding: 20px;
		box-sizing: border-box;
		border: 1px solid gray;
		border-radius: 8px;
		.filter-class {
			display: inline-block;
			box-sizing: border-box;
		}
		.filter-items-box {
			display: inline-block;
			box-sizing: border-box;
			.filter-item {
				display: inline-block;
				box-sizing: border-box;
				margin: 0 6px;
			}
		}
	}
	.filter-items:not(:first-child) {
		margin-top: 20px;
	}
}
hr {
	margin: 20px 0;
}
.file-list {
	.file-items {
		width: 1100px;
		min-height: 400px;
		margin: 0 auto;
		padding: 20px;
		box-sizing: border-box;
		border: 1px solid gray;
		border-radius: 8px;
	}
}
</style>
