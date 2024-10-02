(function(){"use strict";var e={2640:function(e,t,a){var r=a(3751),o=a(641),n=a(33);const l={class:"content-wrapper relative z-10 flex flex-col min-h-screen"},i={class:"bg-white dark:bg-gray-800 shadow-md"},s={class:"container mx-auto px-6 py-3 flex justify-between items-center"},d={class:"flex items-center"},g={key:0},u={key:1};function c(e,t,a,r,c,f){const m=(0,o.g2)("router-link"),p=(0,o.g2)("router-view");return(0,o.uX)(),(0,o.CE)("div",{id:"app",class:(0,n.C4)(["flex flex-col min-h-screen font-sans relative",{dark:c.isDarkMode}])},[(0,o.Lk)("div",l,[(0,o.Lk)("nav",i,[(0,o.Lk)("div",s,[(0,o.bF)(m,{to:"/",class:"text-2xl font-bold text-gray-800 dark:text-white"},{default:(0,o.k6)((()=>t[1]||(t[1]=[(0,o.eW)("CreatiVision")]))),_:1}),(0,o.Lk)("div",d,[(0,o.bF)(m,{to:"/banner",class:"nav-link mx-2"},{default:(0,o.k6)((()=>t[2]||(t[2]=[(0,o.eW)("Banner Generator")]))),_:1}),(0,o.bF)(m,{to:"/video",class:"nav-link mx-2"},{default:(0,o.k6)((()=>t[3]||(t[3]=[(0,o.eW)("Video Generator")]))),_:1}),(0,o.Lk)("button",{onClick:t[0]||(t[0]=(...e)=>f.toggleDarkMode&&f.toggleDarkMode(...e)),class:"ml-4 p-2 rounded-full bg-gray-200 dark:bg-gray-700"},[c.isDarkMode?((0,o.uX)(),(0,o.CE)("span",g,"🌞")):((0,o.uX)(),(0,o.CE)("span",u,"🌙"))])])])]),(0,o.bF)(p),t[4]||(t[4]=(0,o.Lk)("footer",{class:"bg-gray-100 dark:bg-gray-800 py-4 mt-auto"},[(0,o.Lk)("div",{class:"container mx-auto text-center text-gray-600 dark:text-gray-300"}," © 2024 CreatiVision. All rights reserved. ")],-1))])],2)}var f={name:"App",data(){return{isDarkMode:!1}},methods:{toggleDarkMode(){this.isDarkMode=!this.isDarkMode,localStorage.setItem("darkMode",this.isDarkMode),document.documentElement.classList.toggle("dark",this.isDarkMode),document.body.style.transition="background-color 0.5s ease"}},mounted(){this.isDarkMode="true"===localStorage.getItem("darkMode"),document.documentElement.classList.toggle("dark",this.isDarkMode)}},m=a(6262);const p=(0,m.A)(f,[["render",c]]);var b=p,k=a(5220);const h={class:"home"},x={id:"features","data-aos":"fade-up","data-aos-duration":"1000",class:"mb-16 bg-white bg-opacity-90 dark:bg-gray-800 dark:bg-opacity-90 rounded-lg p-8"},y={class:"container mx-auto px-4"},v={class:"grid grid-cols-1 md:grid-cols-2 gap-12"},w={class:"feature-card bg-white dark:bg-gray-800 rounded-lg shadow-md p-8 transition duration-300 hover:shadow-xl transform hover:-translate-y-2"},L={class:"feature-card bg-white dark:bg-gray-800 rounded-lg shadow-md p-8 transition duration-300 hover:shadow-xl transform hover:-translate-y-2"},C={class:"bg-gray-100 dark:bg-gray-700 bg-opacity-90 dark:bg-opacity-90 py-16 rounded-lg"},P={class:"container mx-auto px-4"},W={class:"relative"},M={class:"testimonials-container"},E={ref:"testimonialsWrapper",class:"testimonials-wrapper"},I={class:"text-gray-600 dark:text-gray-300 mb-4"},z={class:"flex items-center"},V=["src","alt"],G={class:"font-semibold text-gray-800 dark:text-white"},_={class:"text-sm text-gray-600 dark:text-gray-400"},F={class:"flex mt-2"};function T(e,t,a,r,l,i){const s=(0,o.g2)("router-link");return(0,o.uX)(),(0,o.CE)("div",h,[t[14]||(t[14]=(0,o.Fv)('<section class="hero bg-gradient-to-r from-blue-500 to-purple-600 text-white py-24 rounded-lg mb-16 relative overflow-hidden" data-v-1101dd1f><canvas id="hero-canvas" class="absolute top-0 left-0 w-full h-full" data-v-1101dd1f></canvas><div class="container mx-auto text-center px-4 relative z-10" data-v-1101dd1f><h1 class="text-5xl md:text-6xl font-bold mb-6 animate-fade-in" data-v-1101dd1f> Welcome to CreatiVision </h1><p class="text-xl md:text-2xl mb-10 animate-fade-in-delay max-w-2xl mx-auto" data-v-1101dd1f> Create stunning banners and videos with the power of AI. </p><a href="#features" class="bg-white text-blue-600 px-8 py-3 rounded-full font-bold text-lg hover:bg-blue-100 transition duration-300 shadow-md" data-v-1101dd1f>Get Started</a></div></section>',1)),(0,o.Lk)("section",x,[(0,o.Lk)("div",y,[t[10]||(t[10]=(0,o.Lk)("h2",{class:"text-3xl md:text-4xl font-bold text-center mb-12 text-gray-800 dark:text-white"}," Our Features ",-1)),(0,o.Lk)("div",v,[(0,o.Lk)("div",w,[t[3]||(t[3]=(0,o.Lk)("div",{class:"text-4xl mb-6 text-blue-500 animate-bounce"},"🎨",-1)),t[4]||(t[4]=(0,o.Lk)("h3",{class:"text-2xl font-semibold mb-4 text-gray-800 dark:text-white"}," Banner Generator ",-1)),t[5]||(t[5]=(0,o.Lk)("p",{class:"text-gray-600 dark:text-gray-300 mb-6"}," Create eye-catching banners for your marketing campaigns with ease. ",-1)),(0,o.bF)(s,{to:"/banner",class:"btn-primary bg-blue-500 text-white font-bold py-2 px-4 rounded"},{default:(0,o.k6)((()=>t[2]||(t[2]=[(0,o.eW)(" Try Now ")]))),_:1})]),(0,o.Lk)("div",L,[t[7]||(t[7]=(0,o.Lk)("div",{class:"text-4xl mb-6 text-purple-500 animate-pulse"},"🎥",-1)),t[8]||(t[8]=(0,o.Lk)("h3",{class:"text-2xl font-semibold mb-4 text-gray-800 dark:text-white"}," Video Generator ",-1)),t[9]||(t[9]=(0,o.Lk)("p",{class:"text-gray-600 dark:text-gray-300 mb-6"}," Generate engaging videos to promote your products or services effortlessly. ",-1)),(0,o.bF)(s,{to:"/video",class:"btn-primary bg-purple-500 text-white font-bold py-2 px-4 rounded"},{default:(0,o.k6)((()=>t[6]||(t[6]=[(0,o.eW)(" Try Now ")]))),_:1})])])])]),(0,o.Lk)("section",C,[(0,o.Lk)("div",P,[t[13]||(t[13]=(0,o.Lk)("h2",{class:"text-3xl md:text-4xl font-bold text-center mb-12 text-gray-800 dark:text-white"}," What Our Users Say ",-1)),(0,o.Lk)("div",W,[(0,o.Lk)("div",M,[(0,o.Lk)("div",E,[((0,o.uX)(!0),(0,o.CE)(o.FK,null,(0,o.pI)(r.testimonials,(e=>((0,o.uX)(),(0,o.CE)("div",{key:e.id,class:"testimonial-card bg-white dark:bg-gray-800 p-6 rounded-lg shadow-sm transition-all duration-300 hover:shadow-lg transform hover:-translate-y-1"},[(0,o.Lk)("p",I,(0,n.v_)(e.comment),1),(0,o.Lk)("div",z,[(0,o.Lk)("img",{src:e.avatar,alt:e.name,class:"w-12 h-12 rounded-full mr-4"},null,8,V),(0,o.Lk)("div",null,[(0,o.Lk)("p",G,(0,n.v_)(e.name),1),(0,o.Lk)("p",_,(0,n.v_)(e.title),1)])]),(0,o.Lk)("div",F,[((0,o.uX)(),(0,o.CE)(o.FK,null,(0,o.pI)(5,(t=>(0,o.Lk)("span",{key:t,class:"text-yellow-400 text-xl"},(0,n.v_)(t<=e.rating?"★":"☆"),1))),64))])])))),128))],512)]),(0,o.Lk)("button",{onClick:t[0]||(t[0]=e=>r.scrollTestimonials("left")),class:"testimonial-arrow left-arrow","aria-label":"Previous testimonial"},t[11]||(t[11]=[(0,o.Lk)("svg",{xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor",class:"w-6 h-6"},[(0,o.Lk)("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M15 19l-7-7 7-7"})],-1)])),(0,o.Lk)("button",{onClick:t[1]||(t[1]=e=>r.scrollTestimonials("right")),class:"testimonial-arrow right-arrow","aria-label":"Next testimonial"},t[12]||(t[12]=[(0,o.Lk)("svg",{xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor",class:"w-6 h-6"},[(0,o.Lk)("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M9 5l7 7-7 7"})],-1)]))])])])])}a(4114);var O=a(953),j={name:"HomePage",setup(){const e=(0,O.KR)([{id:1,name:"Aman kumar",title:"Marketing Manager",comment:"With CreatiVision, we've seen a significant improvement in our ad performance. The videos it creates are vibrant, attention-grabbing, and perfectly tailored for our target audience. Highly recommend!",rating:4,avatar:"/static/images/avatars/aman-avatar.png"},{id:2,name:"Mohammed Zaid Sikander",title:"Small Business Owner",comment:"I can't believe how easy it is to create professional-looking banners and videos. Highly recommended!",rating:4,avatar:"/static/images/avatars/zaid-avatar.png"},{id:3,name:"KS Sohan",title:"Freelance Designer",comment:"The time we save using CreatiVision is incredible. It's like having a design team at your fingertips.",rating:5,avatar:"/static/images/avatars/sohan-avatar.png"},{id:4,name:"Arun Patil",title:"E-commerce Entrepreneur",comment:"CreatiVision has revolutionized our product marketing. The AI-generated content is decent and saves a lot of time.",rating:4.5,avatar:"/static/images/avatars/arun-avatar.png"}]),t=(0,O.KR)(null),a=e=>{const a=t.value,r=a.offsetWidth,o=a.scrollWidth-a.offsetWidth;a.scrollLeft="left"===e?Math.max(0,a.scrollLeft-r):Math.min(o,a.scrollLeft+r)};(0,o.sV)((()=>{r()}));const r=()=>{const e=document.getElementById("hero-canvas"),t=e.getContext("2d");e.width=e.offsetWidth,e.height=e.offsetHeight;const a=[],r=100,o=["#ffffff","#88ccff","#ff88cc"];for(let l=0;l<r;l++)a.push({x:Math.random()*e.width,y:Math.random()*e.height,radius:3*Math.random()+1,color:o[Math.floor(Math.random()*o.length)],speedX:3*Math.random()-1.5,speedY:3*Math.random()-1.5});function n(){requestAnimationFrame(n),t.clearRect(0,0,e.width,e.height),a.forEach((a=>{a.x+=a.speedX,a.y+=a.speedY,(a.x<0||a.x>e.width)&&(a.speedX*=-1),(a.y<0||a.y>e.height)&&(a.speedY*=-1),t.beginPath(),t.arc(a.x,a.y,a.radius,0,2*Math.PI),t.fillStyle=a.color,t.fill()}))}n(),window.addEventListener("resize",(()=>{e.width=e.offsetWidth,e.height=e.offsetHeight}))};return{testimonials:e,testimonialsWrapper:t,scrollTestimonials:a}}};const A=(0,m.A)(j,[["render",T],["__scopeId","data-v-1101dd1f"]]);var D=A;const X={class:"banner-page-container min-h-screen relative"},S={class:"banner-generator max-w-4xl mx-auto my-12 p-8 bg-white dark:bg-gray-800 rounded-xl shadow-2xl relative z-10"},B={class:"form-group"},q={class:"form-group"},J={class:"form-group"},U={class:"form-group"},N={class:"form-group"},H={class:"form-group"},K=["disabled"],Q={key:0,class:"loader ml-2"},R={key:0,class:"mt-8 animate-fade-in"},Y=["src"],$={class:"flex justify-center"},Z=["href"];function ee(e,t,a,l,i,s){return(0,o.uX)(),(0,o.CE)("div",X,[(0,o.Lk)("div",S,[t[17]||(t[17]=(0,o.Lk)("div",{class:"text-center mb-8"},[(0,o.Lk)("h2",{class:"text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500"}," AI Banner Generator "),(0,o.Lk)("p",{class:"text-xl text-gray-300 mt-2"}," Create stunning banners with the power of AI ")],-1)),(0,o.Lk)("form",{onSubmit:t[6]||(t[6]=(0,r.D$)(((...e)=>s.generateBanner&&s.generateBanner(...e)),["prevent"])),class:"space-y-6"},[(0,o.Lk)("div",B,[t[7]||(t[7]=(0,o.Lk)("label",{for:"productImages",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-images mr-2"}),(0,o.eW)("Product Images: ")],-1)),t[8]||(t[8]=(0,o.Lk)("p",{class:"text-sm text-gray-500 dark:text-gray-400 mb-2"},[(0,o.Lk)("i",{class:"fas fa-info-circle mr-1"}),(0,o.eW)("Only PNG or JPG files are allowed. ")],-1)),(0,o.Lk)("input",{type:"file",id:"productImages",onChange:t[0]||(t[0]=(...e)=>s.onFileChange&&s.onFileChange(...e)),accept:".png, .jpg, .jpeg",multiple:"",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,32)]),(0,o.Lk)("div",q,[t[9]||(t[9]=(0,o.Lk)("label",{for:"offer",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-tag mr-2"}),(0,o.eW)("Promotional Offer: ")],-1)),(0,o.bo)((0,o.Lk)("input",{"onUpdate:modelValue":t[1]||(t[1]=e=>i.offer=e),type:"text",id:"offer",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,512),[[r.Jo,i.offer]])]),(0,o.Lk)("div",J,[t[10]||(t[10]=(0,o.Lk)("label",{for:"theme",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-paint-brush mr-2"}),(0,o.eW)("Theme: ")],-1)),(0,o.bo)((0,o.Lk)("input",{"onUpdate:modelValue":t[2]||(t[2]=e=>i.theme=e),type:"text",id:"theme",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,512),[[r.Jo,i.theme]])]),(0,o.Lk)("div",U,[t[11]||(t[11]=(0,o.Lk)("label",{for:"colorPalette",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-palette mr-2"}),(0,o.eW)("Color Palette (comma-separated): ")],-1)),(0,o.bo)((0,o.Lk)("input",{"onUpdate:modelValue":t[3]||(t[3]=e=>i.colorPalette=e),type:"text",id:"colorPalette",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,512),[[r.Jo,i.colorPalette]])]),(0,o.Lk)("div",N,[t[13]||(t[13]=(0,o.Lk)("label",{for:"generatorType",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-cog mr-2"}),(0,o.eW)("Image Generation Model: ")],-1)),(0,o.bo)((0,o.Lk)("select",{"onUpdate:modelValue":t[4]||(t[4]=e=>i.generatorType=e),id:"generatorType",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},t[12]||(t[12]=[(0,o.Lk)("option",{value:"imagen"},"Google Imagen",-1),(0,o.Lk)("option",{value:"huggingface"},"Hugging Face",-1)]),512),[[r.u1,i.generatorType]])]),(0,o.Lk)("div",H,[t[14]||(t[14]=(0,o.Lk)("label",{for:"size",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-expand-arrows-alt mr-2"}),(0,o.eW)("Size (optional, e.g., 1200x628): ")],-1)),(0,o.bo)((0,o.Lk)("input",{"onUpdate:modelValue":t[5]||(t[5]=e=>i.size=e),type:"text",id:"size",placeholder:"1200x628",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-gray-100 dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,512),[[r.Jo,i.size]])]),(0,o.Lk)("button",{type:"submit",disabled:i.isLoading,class:"w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg py-3 px-4 font-bold text-lg hover:from-blue-600 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-all duration-300 transform hover:scale-105 flex items-center justify-center"},[t[15]||(t[15]=(0,o.Lk)("i",{class:"fas fa-magic mr-2"},null,-1)),(0,o.Lk)("span",null,(0,n.v_)(i.isLoading?"Generating...":"Generate Banner"),1),i.isLoading?((0,o.uX)(),(0,o.CE)("div",Q)):(0,o.Q3)("",!0)],8,K)],32),i.result?((0,o.uX)(),(0,o.CE)("div",R,[(0,o.Lk)("img",{src:i.result.image_path,alt:"Generated Banner",class:"w-full rounded-lg shadow-lg mb-4"},null,8,Y),(0,o.Lk)("div",$,[(0,o.Lk)("a",{href:i.result.image_path,download:"generated_banner.png",class:"bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg py-3 px-6 font-bold text-lg hover:from-blue-600 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-all duration-300 transform hover:scale-105 flex items-center justify-center"},t[16]||(t[16]=[(0,o.Lk)("i",{class:"fas fa-download mr-2"},null,-1),(0,o.eW)("Download Banner ")]),8,Z)])])):(0,o.Q3)("",!0)])])}var te={name:"BannerGenerator",data(){return{files:[],offer:"",theme:"",colorPalette:"",generatorType:"imagen",size:"",format:"PNG",result:null,isLoading:!1}},methods:{onFileChange(e){const t=Array.from(e.target.files),a=t.filter((e=>["image/png","image/jpeg"].includes(e.type)));a.length!==t.length?(alert("Please upload only PNG or JPG images."),e.target.value=""):this.files=a},async generateBanner(){this.isLoading=!0;const e=new FormData;if(0===this.files.length)return alert("Please select at least one product image."),void(this.isLoading=!1);this.files.forEach((t=>{e.append("productImages",t)})),e.append("offer",this.offer),e.append("theme",this.theme),e.append("colorPalette",this.colorPalette),e.append("generatorType",this.generatorType),this.size&&e.append("size",this.size),e.append("format",this.format);try{const t=await fetch("/generate_banner",{method:"POST",body:e});if(!t.ok)throw new Error("Network response was not ok");this.result=await t.json()}catch(t){console.error("Error:",t),alert("An error occurred while generating the banner.")}finally{this.isLoading=!1}}}};const ae=(0,m.A)(te,[["render",ee],["__scopeId","data-v-4123f4fa"]]);var re=ae;const oe={class:"video-page-container min-h-screen relative"},ne={key:0,class:"fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50"},le={class:"bg-gradient-to-br from-purple-600 to-blue-500 p-8 rounded-lg shadow-xl animate-fade-in max-w-md"},ie={class:"video-generator max-w-4xl mx-auto my-12 p-8 bg-white dark:bg-gray-800 rounded-xl shadow-2xl relative z-10"},se={class:"form-group"},de={class:"form-group"},ge={class:"form-group"},ue={class:"form-group"},ce={class:"form-group"},fe={class:"form-group"},me=["disabled"],pe={key:0,class:"flex justify-center items-center mt-8"},be={key:1,class:"mt-8 animate-fade-in"},ke=["src"],he={class:"mt-4 text-gray-700 dark:text-gray-300"};function xe(e,t,a,l,i,s){return(0,o.uX)(),(0,o.CE)("div",oe,[i.showPopup?((0,o.uX)(),(0,o.CE)("div",ne,[(0,o.Lk)("div",le,[t[8]||(t[8]=(0,o.Lk)("p",{class:"text-xl text-white font-semibold mb-4"}," 🎬 Lights, camera... not quite action! ",-1)),t[9]||(t[9]=(0,o.Lk)("p",{class:"text-lg text-white mb-6"}," Our video generation feature is still in the editing room. Come back soon for the world premiere! 🍿 ",-1)),(0,o.Lk)("button",{onClick:t[0]||(t[0]=(...e)=>s.closePopup&&s.closePopup(...e)),class:"w-full bg-white text-purple-600 px-6 py-3 rounded-lg font-bold hover:bg-gray-100 transition-colors duration-300"}," Got it! ")])])):(0,o.Q3)("",!0),(0,o.Lk)("div",ie,[t[19]||(t[19]=(0,o.Lk)("div",{class:"text-center mb-8"},[(0,o.Lk)("h2",{class:"text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-500"}," AI Video Generator "),(0,o.Lk)("p",{class:"text-xl text-gray-300 mt-2"}," Create engaging videos with the power of AI ")],-1)),(0,o.Lk)("form",{onSubmit:t[7]||(t[7]=(0,r.D$)(((...e)=>s.generateVideo&&s.generateVideo(...e)),["prevent"])),class:"space-y-6"},[(0,o.Lk)("div",se,[t[10]||(t[10]=(0,o.Lk)("label",{for:"productImage",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-image mr-2"}),(0,o.eW)("Product Image: ")],-1)),(0,o.Lk)("input",{type:"file",id:"productImage",onChange:t[1]||(t[1]=(...e)=>s.onFileChange&&s.onFileChange(...e)),accept:"image/*",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,32)]),(0,o.Lk)("div",de,[t[11]||(t[11]=(0,o.Lk)("label",{for:"offer",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-tag mr-2"}),(0,o.eW)("Promotional Offer: ")],-1)),(0,o.bo)((0,o.Lk)("input",{"onUpdate:modelValue":t[2]||(t[2]=e=>i.offer=e),type:"text",id:"offer",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,512),[[r.Jo,i.offer]])]),(0,o.Lk)("div",ge,[t[12]||(t[12]=(0,o.Lk)("label",{for:"theme",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-paint-brush mr-2"}),(0,o.eW)("Theme: ")],-1)),(0,o.bo)((0,o.Lk)("input",{"onUpdate:modelValue":t[3]||(t[3]=e=>i.theme=e),type:"text",id:"theme",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,512),[[r.Jo,i.theme]])]),(0,o.Lk)("div",ue,[t[13]||(t[13]=(0,o.Lk)("label",{for:"colorPalette",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-palette mr-2"}),(0,o.eW)("Color Palette: ")],-1)),(0,o.bo)((0,o.Lk)("input",{"onUpdate:modelValue":t[4]||(t[4]=e=>i.colorPalette=e),type:"text",id:"colorPalette",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,512),[[r.Jo,i.colorPalette]])]),(0,o.Lk)("div",ce,[t[14]||(t[14]=(0,o.Lk)("label",{for:"size",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-expand-arrows-alt mr-2"}),(0,o.eW)("Size: ")],-1)),(0,o.bo)((0,o.Lk)("input",{"onUpdate:modelValue":t[5]||(t[5]=e=>i.size=e),type:"text",id:"size",placeholder:"1200x628",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,512),[[r.Jo,i.size]])]),(0,o.Lk)("div",fe,[t[15]||(t[15]=(0,o.Lk)("label",{for:"duration",class:"block text-lg font-medium text-gray-700 dark:text-gray-300 mb-2"},[(0,o.Lk)("i",{class:"fas fa-clock mr-2"}),(0,o.eW)("Duration (seconds): ")],-1)),(0,o.bo)((0,o.Lk)("input",{"onUpdate:modelValue":t[6]||(t[6]=e=>i.duration=e),type:"number",id:"duration",required:"",class:"w-full px-4 py-3 text-gray-800 dark:text-gray-200 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300"},null,512),[[r.Jo,i.duration]])]),(0,o.Lk)("button",{type:"submit",disabled:i.isLoading,class:"w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg py-3 px-4 font-bold text-lg hover:from-blue-600 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-all duration-300 transform hover:scale-105"},[t[16]||(t[16]=(0,o.Lk)("i",{class:"fas fa-video mr-2"},null,-1)),(0,o.eW)((0,n.v_)(i.isLoading?"Generating...":"Generate Video"),1)],8,me)],32),i.isLoading?((0,o.uX)(),(0,o.CE)("div",pe,t[17]||(t[17]=[(0,o.Lk)("div",{class:"loader"},null,-1)]))):(0,o.Q3)("",!0),i.result?((0,o.uX)(),(0,o.CE)("div",be,[(0,o.Lk)("video",{src:i.result.video_path,controls:"",class:"w-full rounded-lg shadow-lg"},null,8,ke),(0,o.Lk)("p",he,[t[18]||(t[18]=(0,o.Lk)("strong",null,"Generated Prompt:",-1)),(0,o.eW)(" "+(0,n.v_)(i.result.prompt),1)])])):(0,o.Q3)("",!0)])])}var ye={name:"VideoGenerator",data(){return{file:null,offer:"",theme:"",colorPalette:"",size:"",duration:null,result:null,isLoading:!1,showPopup:!0}},methods:{onFileChange(e){this.file=e.target.files[0]},async generateVideo(){this.isLoading=!0;const e=new FormData;e.append("productImage",this.file),e.append("offer",this.offer),e.append("theme",this.theme),e.append("colorPalette",this.colorPalette),e.append("size",this.size),e.append("duration",this.duration);try{const t=await fetch("/generate_video",{method:"POST",body:e});if(!t.ok)throw new Error("Network response was not ok");this.result=await t.json()}catch(t){console.error("Error:",t),alert("An error occurred while generating the video.")}finally{this.isLoading=!1}},closePopup(){this.showPopup=!1}},mounted(){this.showPopup=!0}};const ve=(0,m.A)(ye,[["render",xe],["__scopeId","data-v-6e22463a"]]);var we=ve;const Le=[{path:"/",component:D},{path:"/banner",component:re},{path:"/video",component:we}],Ce=(0,k.aE)({history:(0,k.LA)(),routes:Le});var Pe=Ce;const We=(0,r.Ef)(b);We.use(Pe),We.mount("#app")}},t={};function a(r){var o=t[r];if(void 0!==o)return o.exports;var n=t[r]={exports:{}};return e[r].call(n.exports,n,n.exports,a),n.exports}a.m=e,function(){var e=[];a.O=function(t,r,o,n){if(!r){var l=1/0;for(g=0;g<e.length;g++){r=e[g][0],o=e[g][1],n=e[g][2];for(var i=!0,s=0;s<r.length;s++)(!1&n||l>=n)&&Object.keys(a.O).every((function(e){return a.O[e](r[s])}))?r.splice(s--,1):(i=!1,n<l&&(l=n));if(i){e.splice(g--,1);var d=o();void 0!==d&&(t=d)}}return t}n=n||0;for(var g=e.length;g>0&&e[g-1][2]>n;g--)e[g]=e[g-1];e[g]=[r,o,n]}}(),function(){a.d=function(e,t){for(var r in t)a.o(t,r)&&!a.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})}}(),function(){a.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={524:0};a.O.j=function(t){return 0===e[t]};var t=function(t,r){var o,n,l=r[0],i=r[1],s=r[2],d=0;if(l.some((function(t){return 0!==e[t]}))){for(o in i)a.o(i,o)&&(a.m[o]=i[o]);if(s)var g=s(a)}for(t&&t(r);d<l.length;d++)n=l[d],a.o(e,n)&&e[n]&&e[n][0](),e[n]=0;return a.O(g)},r=self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))}();var r=a.O(void 0,[504],(function(){return a(2640)}));r=a.O(r)})();
//# sourceMappingURL=app.2b8ccbae.js.map