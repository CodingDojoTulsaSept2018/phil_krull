using Microsoft.AspNetCore.Mvc;

namespace DotnetDemo.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("")]
        public string Index()
        {
            return "Response from Index in Controller";
        }
    }
}