<template>
	<div class="topbox">
		<div class="top">
			<div class="top-tit">
				<span class="xx">道县玉潭精英部资源管理平台&nbsp;-&nbsp;欢迎您</span>
				<div class="userbox">
					<a class="login" href="javascript:" id="top-log">【登录】</a>
					<a class="reg"  href="#">【注册】</a>
				</div>
			</div>
		</div>
	</div>
	<div class="logobox">
		<div class="logo">
			<a href="/">
				<img :src="LogoImg"></a>
		</div>
		<div class="search">
			<div class="ser-input">
				<input type="text" placeholder="输入想搜索内容的关键字" style="width: 360px;">
			</div>
			<div class="ser-btn">
				<button class="btn" type="button" onclick="">
					<el-icon><Search /></el-icon>
				</button>
			</div>
		</div>
	</div>
	<div class="navbox">
		<div class="dh">
			<div class="dh-home">
				<div class="home">
					<el-icon><House /></el-icon>
					<span class="flei">资源导航</span>
				</div>
				<!--左侧菜单与轮换图开始-->
			</div>
			<div class="dhtop">
				<a href="#" class="active">试卷</a>
				<!-- <a href="#">表格</a> -->
			</div>
		</div>
	</div>
	<div class="contentbox">
		<div class="header">
            <span>当前位置: </span>
            <a href="#">玉潭精英部资源网</a> &gt;
        </div>
		<div class="opn-menu">
			<ul class="menu-list">
                <li style="height: 20px;"><span>学科:</span></li>
                <li v-for="item, index in classList" :class="{ 
						active: index == classListItemActiveIndex
					}">
					<a href="#" @click="setClassListItemActiveIndex(index)">{{ item }}</a>
				</li>
            </ul>
			<div class="filter-type">
                <ul class="menu-list">
                    <li><span>类型:</span></li>
                    <li v-for="item, index in tagList" :class="{ 
							active: index == tagListItemActiveIndex
						}">
						<a href="#" @click="setTagListItemActiveIndex(index)">{{ item }}</a>
					</li>
				</ul>
            </div>
		</div>
		<div class="resource">
			<div class="resource-box">
				<p class="search-result">合计<span>7</span>条资源</p>
				<div class="source-card">
					<div class="img-box">
						<img :src="PDFImg">
					</div>
					<div class="text-box">
						<h3>
							<a class="name">部编版语文六年级下册2022-20233学年下学期期末试卷 （含答案）</a>
						</h3>
						<p style="line-height:28px;">
							<span>学科：语文</span>
							<span>分类：试卷</span>
							<span>年级：高一上期</span>
						</p>
						<p>
							<span>时间：2023/6/27 22:32:35</span>
						</p>
					</div>
					<div class="btn-box">
						<a href="#">下载资源</a>
					</div>
				</div>
				<div class="text_nav">
				</div>
			</div>
		</div>
	</div>
	<div class="content-bottom">
    </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import LogoImg from "./assets/logo.png"
import PDFImg from "./assets/pdf.jpg"


const classList = ref<string[]>(["全部", "语文", "数学", "英语"])
const classListItemActiveIndex = ref<number>(0)
const setClassListItemActiveIndex = (index: number) => {
	classListItemActiveIndex.value = index
}

const tagList = ref<string[]>(["全部", "试卷", "导学案"])
const tagListItemActiveIndex = ref<number>(0)
const setTagListItemActiveIndex = (index: number) => {
	tagListItemActiveIndex.value = index
}

</script>

<style scoped lang="less">
.topbox {
	padding: 5px 0;
    background: #f3f3f3;
    border-bottom: #dcdcdc solid 1px;
    height: 40px;
	.top {
		width: 1200px;
		height: 100%;
		margin-left: auto;
		margin-right: auto;
		font-family: "宋体";
		font-size: 16px;
		position: relative;
		.top-tit {
			line-height: 40px;
			display: flex;
			align-items: center;
			justify-content: space-between;
			.userbox {

			}
		}
		.xx {
			color: #00b1a4;
		}
		a {
			color: #757575;
			&:hover {
				color: #ff0000;
			}
		}
	}
}
.logobox {
    width: 1200px;
    margin: auto;
    margin-right: auto;
    height: 100px;
    display: block;
    position: relative;
	.logo {
		float: left;
		margin: 22px 0;
	}
	.search {
		margin-left: 100px;
		float: left;
		margin-top: 35px;
		.ser-input {
			float: left;
			input {
				height: 34px;
				border: 1px solid #14c1b5;
				padding-left: 10px;
				outline: none;
			}
		}
		.ser-btn {
			float: left;
			.btn {
				width: 68px;
				height: 36px;
				background-color: #00d3c4;
				border: none;
				outline: none;
				cursor: pointer;
			}
			.el-icon {
				width: 30px;
				font-size: 18px;
				font-weight: bold;
				color: white;
			}
		}
	}
}
.navbox {
    background-color: #00d3c4;
    height: 50px;
    clear: both;
    display: block;
    position: relative;
	.dh {
		width: 1200px;
		height: 100%;
		margin-left: auto;
		margin-right: auto;
		font-family: "微软雅黑";
		font-size: 18px;
		color: #fff;
		position: relative;
		display: flex;
		justify-content: start;
		.dh-home {
			display: flex;
			height: 100%;
			width: 200px;
			justify-content: center;
			align-items: center;
			.home {
				display: flex;
				align-items: center;
				.el-icon {
					font-size: 22px;
				}
				.flei {
					margin-left: 10px;
					display: inline-block;
					font-size: 24px;
				}
			}
		}
		.dhtop {
			position: relative;
		}
		a {
			font-family: "微软雅黑";
			font-size: 17px;
			color: #fff;
			line-height: 50px;
			padding: 0 15px;
			line-height: 50px;
			display: inline-block;
			height: 100%;
			&:hover {
				background-color: #2ab3a9;
			}
			&.active {
				background-color: #2ab3a9;
			}
		}
	}
}
.contentbox {
    width: 1200px;
    margin: 0 auto;
	margin-top: 20px;
	.opn-menu {
		border: 1px solid #ddd;
		border-radius: 2px;
		font-size: 13px;
		color: #444;
	}
	.header {
		font-size: 14px;
		padding: 10px 0;
		a {
			color: #999;
		}
	}
	.menu-list {
		font-size: 16px;
		padding: 10px 0;
		width: 1140px;
		margin: 0 auto;
		border-bottom: 1px dashed #dbdbdb;
		display: flex;
		justify-content: start;
		li {
			padding: 6px 12px;
			margin: 5px 3px;
			&:first-child {
				margin-right: 0;
			}
			&.active {
				background-color: #14c1b5;
				border-radius: 5px;
			}
		}
	}
	.resource {
		margin-top: 40px;
		overflow: hidden;
		.resource-box {
			margin-bottom: 20px;
			border: 1px solid #dbdbdb;
			border-radius: 6px;
			min-height: 400px;
			.search-result {
				font-size: 16px;
				color: #444;
				padding: 16px 20px;
				border-bottom: 1px solid #ddd;
				span {
					color: red;
				}
			}
			.source-card {
				width: 95%;
				margin: 0 auto;
				padding: 30px 0;
				border-bottom: 1px dashed #ddd;
				clear: both;
				display: flex;
				align-items: center;
				.img-box {
					width: 60px;
					height: 60px;
					font-size: 0;
				}
				.text-box {
					margin-left: 55px;
					flex: 1;
					.name {
						font-weight: bold;
						display: inline-block;
						width: 600px;
						color: #444;
						font-size: 18px;
						font-weight: bold;
						white-space: nowrap;
						text-overflow: ellipsis;
						overflow: hidden;
					}
					p {
						margin: 5px 0;
						span:not(:first-child) {
							margin-left: 22px;
						}
					}
				}
				.btn-box {
					margin: 10px 20px;
					a {
						font-size: 18px;
						padding: 5px 12px;
						border-radius: 5px;
						color: #fff;
						background-color: #ffb304;
					}
				}
			}
			.text_nav {
				width: 100%;
				text-align: center;
				padding: 20px 0px;
			}
		}
	}
}
.content-bottom {
	margin-top: 200px;
    background: #f5f5f5;
    border-top: 1px solid #ababab;
    border-bottom: 1px solid #dfdfdf;
	min-height: 240px;
}
</style>
