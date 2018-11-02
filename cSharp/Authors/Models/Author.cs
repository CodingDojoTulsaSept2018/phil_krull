using System;
using System.ComponentModel.DataAnnotations;

namespace Authors.Models
{
    public class Author
    {
        [Display(Name = "Author Name:")]
        [Required(ErrorMessage="Name field is required!")]
        [MinLength(2)]
        public string Name { get; set; }
        public DateTime CreatedAt { get; set; }
        public DateTime UpdatedAt { get; set; }

        // update time stamps on create
        public Author()
        {
            CreatedAt = DateTime.Now;
            UpdatedAt = DateTime.Now;
        }
        public Author(string Name)
        {
            this.Name = Name;
            CreatedAt = DateTime.Now;
            UpdatedAt = DateTime.Now;
        }
    }
}